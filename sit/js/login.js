(() => {
  let reg = false;
  const $ = id => document.getElementById(id);
  const form = $('authForm');
  const render = () => {
    $('heading').textContent = reg ? 'Buat akun baru' : 'Masuk ke SIT';
    $('cta').textContent = reg ? 'Daftar' : 'Masuk';
    $('ask').textContent = reg ? 'Sudah punya akun?' : 'Belum punya akun?';
    $('swap').textContent = reg ? 'Masuk' : 'Register';
    document.querySelectorAll('.reg-only').forEach(el => el.classList.toggle('d-none', !reg));
    form.classList.remove('was-validated');
    ['nim', 'pw', 'pw2'].forEach(i => $(i).setCustomValidity(''));
  };
  $('swap').addEventListener('click', () => { reg = !reg; render(); });

  form.addEventListener('submit', e => {
    e.preventDefault();
    const nim = $('nim').value.trim(), pw = $('pw').value;
    $('nim').setCustomValidity(/^\d{4}[0-9A-Za-z]{2,10}$/.test(nim) ? '' : 'NIM tidak valid');
    $('pw').setCustomValidity(pw.length >= 8 ? '' : 'Minimal 8 karakter');
    $('n').required = reg; $('pw2').required = reg;
    $('pw2').setCustomValidity(reg && $('pw2').value !== pw ? 'Tidak sama' : '');
    form.classList.add('was-validated');
    if (!form.checkValidity()) return;

    const d = SIT.get();
    if (reg && $('n').value.trim()) d.profile.n = $('n').value.trim();
    d.profile.nim = nim; SIT.save();
    location.href = 'kalender.html';
  });
  render();
})();
