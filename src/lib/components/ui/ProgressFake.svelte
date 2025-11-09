<script lang="ts">
  export let playing = false;
  let val = 0; let t: any;
  $: if (playing) {
    clearInterval(t); val = 0;
    t = setInterval(()=> val = Math.min(99, val + (Math.random()*7+3)), 180);
  } else { clearInterval(t); }
</script>

<div class="w-full h-2 bg-white/8 rounded-full overflow-hidden">
  <div class="h-full bg-neon transition-[width] duration-200" style={`width:${val}%`}></div>
</div>
