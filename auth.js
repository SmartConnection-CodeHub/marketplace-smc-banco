/* ===========================================================
   Marketplace SMC · Banco · Auth Gate (light barrier)
   ⚠️ NO ES seguridad criptográfica · es barrera contra
   visitantes casuales. Cualquiera con devtools puede bypass.
   Si necesitás seguridad real · migrar a repo privado + Pro
   o a S3 + basic auth.
   =========================================================== */
(function(){
  // SHA-256 del PIN "hoku" (nombre del agente IA · Westie de Guillermo)
  const PIN_HASH = '2b14ee3fcd60f65d2e248beaeb53f6e2070fe6ceaef2a21a1010dc3b10d18c69';

  async function sha256(text){
    const buf = new TextEncoder().encode(text);
    const hash = await crypto.subtle.digest('SHA-256', buf);
    return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, '0')).join('');
  }

  function setAuthed(){ sessionStorage.setItem('smc_banco_auth', 'ok'); }
  function isAuthed(){ return sessionStorage.getItem('smc_banco_auth') === 'ok'; }

  if (isAuthed()) return;

  // Bloquear contenido hasta auth
  document.documentElement.style.visibility = 'hidden';

  function init(){
    document.body.innerHTML = `
      <div id="smc-gate" style="position:fixed;inset:0;background:linear-gradient(135deg,#0F172A 0%,#0F766E 50%,#00C1C1 100%);z-index:99999;display:flex;align-items:center;justify-content:center;font-family:'Inter',-apple-system,sans-serif">
        <div style="background:white;padding:48px 56px;border-radius:20px;max-width:420px;width:90%;box-shadow:0 30px 60px rgba(0,0,0,0.3)">
          <div style="font-size:12px;letter-spacing:4px;color:#00C1C1;font-weight:700;text-transform:uppercase;margin-bottom:14px">◆ SMART CONNECTION</div>
          <h1 style="font-size:32px;font-weight:800;margin:0 0 8px;color:#0F172A;letter-spacing:-1px">Banco de<br>Documentos</h1>
          <p style="font-size:13px;color:#64748B;margin:0 0 28px">Acceso restringido · ingresa el PIN para continuar.</p>
          <input id="smc-pin" type="password" inputmode="numeric" autocomplete="off" placeholder="PIN"
            style="width:100%;padding:14px 18px;font-size:18px;border:2px solid #E2E8F0;border-radius:10px;outline:none;letter-spacing:6px;text-align:center;font-family:'JetBrains Mono',monospace"
            onfocus="this.style.borderColor='#00C1C1'" onblur="this.style.borderColor='#E2E8F0'"/>
          <div id="smc-err" style="color:#EF4444;font-size:12px;margin-top:10px;height:16px;text-align:center"></div>
          <button id="smc-submit" style="width:100%;margin-top:18px;padding:14px;background:#00C1C1;color:white;border:none;border-radius:10px;font-size:14px;font-weight:700;letter-spacing:1px;text-transform:uppercase;cursor:pointer">Acceder</button>
          <p style="font-size:11px;color:#94A3B8;margin:24px 0 0;text-align:center">Contenido confidencial · uso interno SMC</p>
        </div>
      </div>
    `;
    document.documentElement.style.visibility = 'visible';

    const input = document.getElementById('smc-pin');
    const err   = document.getElementById('smc-err');
    const btn   = document.getElementById('smc-submit');

    setTimeout(() => input.focus(), 100);

    async function check(){
      const pin = input.value.trim();
      if (!pin){ err.textContent = 'Ingresa el PIN'; return; }
      const h = await sha256(pin);
      if (h === PIN_HASH){
        setAuthed();
        location.reload();
      } else {
        err.textContent = 'PIN incorrecto';
        input.value = '';
        input.focus();
      }
    }

    btn.addEventListener('click', check);
    input.addEventListener('keydown', e => { if (e.key === 'Enter') check(); });
  }

  if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
