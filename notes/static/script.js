function printPage() {
  // Scanner le code QR
        var qrCanvas = document.createElement("canvas");
        var qrContext = qrCanvas.getContext("2d");
        qrCanvas.width = qrCodeEl.offsetWidth;
        qrCanvas.height = qrCodeEl.offsetHeight;
        qrContext.drawImage(qrCodeEl, 0, 0, qrCanvas.width, qrCanvas.height);
        var imageData = qrContext.getImageData(0, 0, qrCanvas.width, qrCanvas.height);
        var code = jsQR(imageData.data, imageData.width, imageData.height);
                
  // Vérifier le code QR et imprimer la page
        if (code && code.data === "http://example.com") {
            window.print();
        } else {
            alert("Le code QR est invalide");
        }
    }