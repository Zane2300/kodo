<script lang="ts">
  import { CATEGORIES } from '$lib/data/tools';
  import { onMount } from 'svelte';

  let open = false;
  let q = '';
  let inputEl: HTMLInputElement;

  const entries = CATEGORIES.flatMap(c => [
    { type: 'category', title: c.title, path: `/${c.slug}` },
    ...c.tools.map(t => ({ type: 'tool', title: `${c.title}: ${t.title}`, path: `/${c.slug}/${t.slug}` }))
  ]);

  $: filtered = q
    ? entries.filter(e => e.title.toLowerCase().includes(q.toLowerCase())).slice(0, 12)
    : entries.slice(0, 12);

  function onKey(e: KeyboardEvent) {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault(); open = !open;
      queueMicrotask(()=> inputEl?.focus());
    } else if (e.key === 'Escape') { open = false; }
  }
  onMount(() => window.addEventListener('keydown', onKey));
</script>

{#if open}
  <div class="fixed inset-0 bg-black/60 backdrop-blur-sm z-50" on:click={()=>open=false}>
    <div class="mx-auto mt-24 w-full max-w-xl rounded-2xl bg-bg ring-1 ring-white/10 p-3" on:click|stopPropagation>
      <input bind:this={inputEl} bind:value={q} placeholder="Search (Ctrl/Cmd + K)…"
             class="w-full bg-black/40 rounded-xl px-3 py-2 outline-none"
             autocomplete="off" />
      <div class="mt-2 max-h-80 overflow-auto space-y-1">
        {#each filtered as e}
          <a href={e.path}
             class="block px-3 py-2 rounded-lg hover:bg-white/5 text-sm">
            {e.title}
          </a>
        {/each}
        {#if !filtered.length}
          <div class="px-3 py-2 text-sm text-mute">No results</div>
        {/if}
      </div>
      <div class="mt-2 text-[11px] text-mute">Tip: press Esc to close</div>
    </div>
  </div>
{/if}
