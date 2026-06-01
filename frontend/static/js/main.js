// ================= GLOBAL =================
let selectedSpecies = null;
let selectedFile = null;
let lastDetections = [];
let cameraStream = null;

function getSlug(label) {
  if (label.toLowerCase().includes("ringworm")) return "ringworm";
  if (label.toLowerCase().includes("scabies") || label.toLowerCase().includes("mange")) return "scabies";
  if (label.toLowerCase().includes("malassezia")) return "malassezia";
  return "ringworm";
}

function normalizeDisplayLabel(label) {
  if (!label) return label;

  const lower = label.toLowerCase();

  if (lower.includes("scabies") || lower.includes("mange")) {
    return "Scabies/Mange";
  }

  return label;
}

// ================= PILIH HEWAN =================
window.choosePet = function (pet) {
  selectedSpecies = pet;

  console.log("Species:", selectedSpecies);

  document.getElementById('selectPet').classList.add('hidden');
  document.getElementById('uploadSection').classList.remove('hidden');
};

window.goBack = function () {
  selectedSpecies = null;
  selectedFile = null;

  document.getElementById('uploadSection').classList.add('hidden');
  document.getElementById('selectPet').classList.remove('hidden');

  document.getElementById("preview").classList.add("hidden");
  document.getElementById("uploadBox").classList.remove("hidden");
  document.getElementById("cameraBtn").classList.remove("hidden"); // <-- tambahin
  document.getElementById("preview").classList.add("hidden");
  document.getElementById("preview").src = "";

  document.getElementById("afterState").classList.add("hidden");
  document.getElementById("beforeState").classList.remove("hidden");

  document.getElementById("result").innerHTML = "";

  if (cameraStream) {
    cameraStream.getTracks().forEach(track => track.stop());
    cameraStream = null;
  }

  document.getElementById("cameraContainer").classList.add("hidden");

  window.scrollTo({ top: 0, behavior: "smooth" });
};

window.onload = function () {
  const input = document.getElementById("imageInput");
  const preview = document.getElementById("preview");
  const resultDiv = document.getElementById("result");
  const loading = document.getElementById("loading");
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  const uploadBox = document.getElementById("uploadBox");
  const changeBtn = document.getElementById("changeBtn");
  const cameraBtn = document.getElementById("cameraBtn");
  const cameraContainer = document.getElementById("cameraContainer");
  const video = document.getElementById("video");

  cameraBtn.addEventListener("click", async () => {

  try {

    if (cameraStream) {
      cameraStream.getTracks().forEach(track => track.stop());
    }

    cameraStream =
      await navigator.mediaDevices.getUserMedia({
        video: true
      });

    video.srcObject = cameraStream;

    cameraContainer.classList.remove("hidden");

    uploadBox.classList.add("hidden");
    cameraBtn.classList.add("hidden");

  } catch (err) {
    alert("Tidak dapat mengakses kamera");
    console.error(err);
  }

});

document
  .getElementById("captureBtn")
  .addEventListener("click", () => {

    const tempCanvas =
      document.createElement("canvas");

    tempCanvas.width = video.videoWidth;
    tempCanvas.height = video.videoHeight;

    const tempCtx =
      tempCanvas.getContext("2d");

    tempCtx.drawImage(
      video,
      0,
      0,
      tempCanvas.width,
      tempCanvas.height
    );

    tempCanvas.toBlob((blob) => {

      selectedFile = new File(
        [blob],
        "capture.jpg",
        { type: "image/jpeg" }
      );

      preview.src =
        URL.createObjectURL(blob);

      preview.classList.remove("hidden");

      uploadBox.classList.add("hidden");
      document .getElementById("previewActions") .classList.remove("hidden");

      preview.onload = () => {
        canvas.width = preview.clientWidth;
        canvas.height = preview.clientHeight;
      };

      if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
        cameraStream = null;
      }

      cameraContainer.classList.add("hidden");
    }, "image/jpeg");

});

  // ================= RESIZE =================
  window.addEventListener("resize", () => {
  const resultImage = document.getElementById("resultImage");

  if (resultImage && !document.getElementById("afterState").classList.contains("hidden")) {
    drawDetectionsOnResult(lastDetections);
  }
});

  // ================= PREVIEW =================
  input.addEventListener("change", function () {
    selectedFile = input.files[0];

    if (selectedFile) {
      preview.src = URL.createObjectURL(selectedFile);
      preview.classList.remove("hidden");

      document .getElementById("previewActions") .classList.remove("hidden");

      uploadBox.classList.add("hidden");
      cameraBtn.classList.add("hidden");

      preview.onload = () => {
        canvas.width = preview.clientWidth;
        canvas.height = preview.clientHeight;
      };

      if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
        cameraStream = null;
      }

      cameraContainer.classList.add("hidden");
    }
  });

  // ================= RESET =================
  window.resetUpload = function () {
    selectedFile = null;
    input.value = "";

    preview.classList.add("hidden");
    preview.src = "";
    uploadBox.classList.remove("hidden");
    document.getElementById("previewActions").classList.add("hidden");
    cameraBtn.classList.remove("hidden");

    document.getElementById("afterState").classList.add("hidden");
    document.getElementById("beforeState").classList.remove("hidden");

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    resultDiv.innerHTML = "";

    if (cameraStream) {
      cameraStream
        .getTracks()
        .forEach(track => track.stop());

      cameraStream = null;
    }

    cameraContainer.classList.add("hidden");
  };

  // ================= DRAW BOX (PREVIEW) =================
  function drawDetections(detections) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const scaleX = canvas.width / preview.naturalWidth;
  const scaleY = canvas.height / preview.naturalHeight;

  detections.forEach((det) => {
    let { x1, y1, x2, y2 } = det.bbox;

    x1 *= scaleX;
    x2 *= scaleX;
    y1 *= scaleY;
    y2 *= scaleY;

    const width = x2 - x1;
    const height = y2 - y1;

    const displayLabel = normalizeDisplayLabel(det.display_label || det.label);
    const color = getBBoxColor(displayLabel);

    ctx.strokeStyle = color;
    ctx.lineWidth = 3;
    ctx.strokeRect(x1, y1, width, height);

    ctx.fillStyle = color;
    ctx.fillRect(x1, y1 - 20, 160, 20);

    ctx.fillStyle = "white";
    ctx.font = "14px Arial";
    ctx.fillText(
      `${displayLabel} ${(det.confidence * 100).toFixed(1)}%`,
      x1 + 5,
      y1 - 5
    );
  });
}

  // ================= DRAW BOX (RESULT - FIX UTAMA) =================
 function drawDetectionsOnResult(detections) {
  const resultCanvas = document.getElementById("resultCanvas");
  const resultImage = document.getElementById("resultImage");
  const rctx = resultCanvas.getContext("2d");

  resultCanvas.width = resultImage.clientWidth;
  resultCanvas.height = resultImage.clientHeight;

  const scaleX = resultCanvas.width / resultImage.naturalWidth;
  const scaleY = resultCanvas.height / resultImage.naturalHeight;

  rctx.clearRect(0, 0, resultCanvas.width, resultCanvas.height);

  detections.forEach((det) => {
    let { x1, y1, x2, y2 } = det.bbox;

    x1 *= scaleX;
    x2 *= scaleX;
    y1 *= scaleY;
    y2 *= scaleY;

    const width = x2 - x1;
    const height = y2 - y1;

    const displayLabel = normalizeDisplayLabel(det.display_label || det.label);
    const color = getBBoxColor(displayLabel);

    rctx.strokeStyle = color;
    rctx.lineWidth = 3;
    rctx.strokeRect(x1, y1, width, height);

    rctx.fillStyle = color;
    rctx.fillRect(x1, y1 - 20, 160, 20);

    rctx.fillStyle = "white";
    rctx.font = "14px Arial";
    rctx.fillText(
      `${displayLabel} ${(det.confidence * 100).toFixed(1)}%`,
      x1 + 5,
      y1 - 5
    );
  });
}

  // ================= ANALYZE =================
  window.analyzeImage = async function () {
    if (!selectedFile) {
      alert("Upload gambar dulu!");
      return;
    }

    if (!selectedSpecies) {
      alert("Pilih jenis hewan dulu!");
      return;
    }

    loading.classList.remove("hidden");

    const formData = new FormData();
    formData.append("image", selectedFile);
    formData.append("species", selectedSpecies);

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      loading.classList.add("hidden");

      lastDetections = data.detections;

      if (data.detections.length === 0) {

        // switch ke result state
        document.getElementById("beforeState").classList.add("hidden");
        document.getElementById("afterState").classList.remove("hidden");

        // tampilkan gambar tetap
        const resultImage = document.getElementById("resultImage");
        resultImage.src = preview.src;

        resultImage.onload = () => {
          const resultCanvas = document.getElementById("resultCanvas");
          const rctx = resultCanvas.getContext("2d");
          rctx.clearRect(0, 0, resultCanvas.width, resultCanvas.height);
        };

        // isi teks
        const labelEl = document.getElementById("resultLabel");
        labelEl.innerText = "Tidak terdeteksi";
        labelEl.className =
          "mt-2 inline-block px-3 py-1 rounded-full text-sm font-semibold bg-gray-100 text-gray-600";

        document.getElementById("resultConfidence").innerText = "-";
        document.getElementById("resultDesc").innerText =
          "Tidak ditemukan indikasi penyakit pada gambar yang diunggah.";

        return;
      }

      const det = data.detections[0];

      drawDetections(data.detections);

      const label = normalizeDisplayLabel(det.display_label || det.label);
      const slug = getSlug(label);
      const colorClass = getColor(label);
      const description = getDescription(label);

      // switch UI
      document.getElementById("beforeState").classList.add("hidden");
      document.getElementById("afterState").classList.remove("hidden");

      // set image
      const resultImage = document.getElementById("resultImage");
      resultImage.src = preview.src;

      // 🔥 FIX: render bbox setelah image ready
      resultImage.onload = () => {
        drawDetectionsOnResult(data.detections);
      };

      // text
      const labelEl = document.getElementById("resultLabel");
      labelEl.innerText = label;
      labelEl.className =
        `mt-2 inline-block px-3 py-1 rounded-full text-sm font-semibold ${colorClass}`;

      document.getElementById("resultConfidence").innerText =
        (det.confidence * 100).toFixed(1) + "%";

      document.getElementById("resultDesc").innerText = description;

      const readMoreBtn = document.getElementById("readMoreBtn");

      readMoreBtn.href =
        `/detail/${slug}?from=detect&species=${selectedSpecies}&confidence=${(det.confidence * 100).toFixed(1)}`;

    } catch (err) {
      loading.classList.add("hidden");
      alert("Error: " + err);
    }
    
  };

  function getColor(label) {
    if (label.toLowerCase().includes("ringworm")) {
      return "bg-purple-100 text-purple-700";
    }
    if (label.toLowerCase().includes("scabies") || label.toLowerCase().includes("mange")) {
      return "bg-red-100 text-red-700";
    }
    return "bg-gray-100 text-gray-700";
  }

  function getBBoxColor(label) {
  if (!label) return "red";

  const lower = label.toLowerCase();

  if (lower.includes("ringworm")) {
    return "#a855f7"; // ungu
  }

  if (lower.includes("scabies") || lower.includes("mange")) {
    return "#ef4444"; // merah
  }

  return "red"; // default tetep merah kayak sekarang
}

  function getDescription(label) {
    if (label.toLowerCase().includes("ringworm")) {
      return "Infeksi jamur yang menyebabkan bercak melingkar dan kerontokan bulu.";
    }
    if (label.toLowerCase().includes("scabies") || label.toLowerCase().includes("mange")) {
     return "Scabies/Mange adalah penyakit kulit akibat infestasi tungau yang menyebabkan gatal, iritasi, kerontokan bulu, dan peradangan pada kulit.";
    }
    return "Deskripsi tidak tersedia.";
  }

  // DRAG & DROP
  uploadBox.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadBox.classList.add("border-yellow-400", "bg-[#fff9e6]");
  });

  uploadBox.addEventListener("dragleave", () => {
    uploadBox.classList.remove("border-yellow-400", "bg-[#fff9e6]");
  });

  uploadBox.addEventListener("drop", (e) => {
    e.preventDefault();

    uploadBox.classList.remove("border-yellow-400", "bg-[#fff9e6]");

    const file = e.dataTransfer.files[0];

    if (file && file.type.startsWith("image/")) {
      selectedFile = file;

      preview.src = URL.createObjectURL(file);
      preview.classList.remove("hidden");

      uploadBox.classList.add("hidden");
      document .getElementById("previewActions") .classList.remove("hidden");
      cameraBtn.classList.add("hidden");

      preview.onload = () => {
        canvas.width = preview.clientWidth;
        canvas.height = preview.clientHeight;
      };
    }
  });

};