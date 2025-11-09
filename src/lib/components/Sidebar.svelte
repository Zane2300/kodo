<script lang="ts">
  import { CATEGORIES } from '$lib/data/tools';
  import { Icon } from 'lucide-svelte';
  import { page } from '$app/stores';
  $: path = $page.url.pathname;
</script>

<nav class="sticky top-4 space-y-2">
  {#each CATEGORIES as c}
    <a href={"/" + c.slug}
       class="flex items-center gap-3 rounded-xl px-3 py-2 transition
              hover:bg-white/5 ring-1 ring-transparent
              {path.startsWith('/'+c.slug)
                ? 'bg-white/5 ring-white/10 shadow-[0_0_14px_rgba(34,211,238,.15)]'
                : ''}">
      <Icon name={c.icon} class="w-4 h-4 text-neon shrink-0" strokeWidth={2} />
      <span class="text-sm">{c.title}</span>
    </a>
  {/each}
</nav>
