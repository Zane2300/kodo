<script lang="ts">
  import { Icon } from 'lucide-svelte';
  import { animate } from 'motion';
  import { onMount } from 'svelte';

  export let href = '#';
  export let title = '';
  export let icon = 'Square';   // nombre de icono lucide
  export let desc = '';
  export let delay = 0;         // para cascada

  let el: HTMLElement | null = null;

  onMount(() => {
    if (el) animate(
      el,
      { opacity: [0, 1], y: [8, 0] },
      { duration: 0.22, delay }
    );
  });
</script>

<a bind:this={el} {href}
   class="group block rounded-2xl px-5 py-3 bg-black/40 ring-1 ring-white/10
          hover:ring-neon/50 transition shadow-lg
          hover:shadow-[0_0_18px_rgba(34,211,238,.25)]">
  <div class="flex items-center gap-3">
    <!-- strokeWidth un pelín más grueso para que siempre se perciba -->
    <Icon name={icon} class="w-5 h-5 text-neon shrink-0" strokeWidth={2} aria-hidden="true" />
    <h3 class="font-medium leading-tight">{title}</h3>
  </div>
  {#if desc}<p class="mt-2 text-sm text-mute">{desc}</p>{/if}
</a>
