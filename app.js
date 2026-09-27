(()=>{
  const nav=document.getElementById('nav'), bar=document.getElementById('progresso');
  let tick=false;
  const onScroll=()=>{
    if(tick) return; tick=true;
    requestAnimationFrame(()=>{
      const y=scrollY, h=document.documentElement.scrollHeight-innerHeight;
      bar.style.transform=`scaleX(${h>0?y/h:0})`;
      nav.classList.toggle('solida',y>60);
      tick=false;
    });
  };
  addEventListener('scroll',onScroll,{passive:true}); onScroll();

  const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}}),{threshold:.15,rootMargin:'0px 0px -40px 0px'});
  document.querySelectorAll('.rv').forEach(el=>io.observe(el));

  const trilho=document.getElementById('trilho');
  document.querySelectorAll('.setas button').forEach(b=>b.addEventListener('click',()=>{
    const f=trilho.querySelector('figure');
    trilho.scrollBy({left:(f.offsetWidth+14)*Number(b.dataset.dir),behavior:'smooth'});
  }));

  const box=document.getElementById('videoBox'), video=document.getElementById('video');
  document.getElementById('videoPlay').addEventListener('click',()=>{box.classList.add('tocando');video.controls=true;video.play()});
  video.addEventListener('play',()=>box.classList.add('tocando'));

  const c=document.getElementById('contador'), s0=c.dataset.suf, suf=(s0.length>1?' ':'')+s0;
  const reduz=matchMedia('(prefers-reduced-motion: reduce)').matches;
  new IntersectionObserver((es,o)=>es.forEach(e=>{
    if(!e.isIntersecting) return; o.disconnect();
    const alvo=+c.dataset.alvo;
    if(reduz){c.textContent=alvo+suf;return}
    const t0=performance.now(), dur=2200;
    const passo=t=>{const p=Math.min((t-t0)/dur,1);c.textContent=Math.round(alvo*(1-Math.pow(1-p,3)))+suf;if(p<1)requestAnimationFrame(passo)};
    requestAnimationFrame(passo);
  }),{threshold:.5}).observe(c);

  const som=document.getElementById('som'), audio=document.getElementById('audio'), somTxt=document.getElementById('somTxt');
  const estado=on=>{som.setAttribute('aria-pressed',on);somTxt.textContent=on?som.dataset.pausar:som.dataset.tocar};
  som.addEventListener('click',()=>{if(audio.paused){video.pause();audio.play()}else audio.pause()});
  audio.addEventListener('play',()=>estado(true));
  audio.addEventListener('pause',()=>estado(false));
  audio.addEventListener('ended',()=>estado(false));
  video.addEventListener('play',()=>audio.pause());
})();
