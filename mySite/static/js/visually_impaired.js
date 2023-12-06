if (!window.isvekInitialized) {
    window.isvekInitialized = true;
    document.addEventListener('DOMContentLoaded', function() {
      new isvek.Bvi({
        target: '.bvi-open',
        fontSize: 24,
        images: 'grayscale',
      });
    });
  }
  