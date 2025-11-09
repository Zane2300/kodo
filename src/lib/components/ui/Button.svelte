<script lang="ts"> export let kind:'primary'|'ghost'='primary'; </script>
<button class="px-4 py-2 rounded-xl text-sm transition
  {kind==='primary'
    ? 'bg-acc/90 hover:bg-acc text-white'
    : 'bg-white/5 hover:bg-white/10 ring-1 ring-white/10'}">
  <slot />
</button>
