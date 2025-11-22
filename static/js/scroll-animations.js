// Scroll animations for sections using IntersectionObserver
// Applies fade-up on enter and reverse on exit by toggling Tailwind utility classes

document.addEventListener('DOMContentLoaded', () => {
  const animatedEls = Array.from(document.querySelectorAll('[data-animate]'));
  if (animatedEls.length === 0) return;

  const ensureTransition = (el) => {
    // Não definir a duração aqui para evitar sobrescrever classes do template.
    el.classList.add('transition-all', 'ease-out');
  };

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const el = entry.target;
        ensureTransition(el);
        const type = el.getAttribute('data-animate') || 'fade-up';

        if (entry.isIntersecting) {
          // Enter animation
          switch (type) {
            case 'fade-in':
              el.classList.remove('opacity-0');
              el.classList.add('opacity-100');
              break;
            case 'fade-up':
            default:
              el.classList.remove('opacity-0', 'translate-y-6');
              el.classList.add('opacity-100', 'translate-y-0');
              break;
          }
        } else {
          // Exit animation (hide when leaving viewport)
          switch (type) {
            case 'fade-in':
              el.classList.remove('opacity-100');
              el.classList.add('opacity-0');
              break;
            case 'fade-up':
            default:
              el.classList.remove('opacity-100', 'translate-y-0');
              el.classList.add('opacity-0', 'translate-y-6');
              break;
          }
        }
      });
    },
    {
      // Disparar mais cedo quando o elemento se aproxima do viewport
      threshold: 0.05,
      rootMargin: '0px 0px 15% 0px',
    }
  );

  // Initialize all elements as hidden to avoid flashes
  animatedEls.forEach((el) => {
    const type = el.getAttribute('data-animate') || 'fade-up';
    ensureTransition(el);
    if (type === 'fade-in') {
      el.classList.add('opacity-0');
    } else {
      el.classList.add('opacity-0', 'translate-y-6');
    }
    observer.observe(el);
  });
});