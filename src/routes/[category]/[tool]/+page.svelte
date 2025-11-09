<script lang="ts">
  import { CATEGORIES } from '$lib/data/tools';
  import FileDropzone from '$lib/components/FileDropzone.svelte';
  import Button from '$lib/components/ui/Button.svelte';
  import ProgressFake from '$lib/components/ui/ProgressFake.svelte';
  import Spinner from '$lib/components/ui/Spinner.svelte';
  import { page } from '$app/stores';

  let files: File[] = [];
  let loading = false;

  // 👇 todo reactivo
  $: params = $page.params;
  $: cat   = CATEGORIES.find((c) => c.slug === params.category);
  $: tool  = cat?.tools.find((t) => t.slug === params.tool);

  function startFake() {
    if (!files.length) return;
    loading = true;
    setTimeout(() => (loading = false), 2600 + Math.random() * 1200);
  }
  function clearSel() { files = []; }
</script>

{#if tool}
  <h1 class="text-2xl mb-4">{tool.title}</h1>

  <div class="space-y-4">
    <FileDropzone on:select={(e)=> (files = e.detail)} />

    <div class="flex items-center gap-3">
      <Button on:click={startFake} kind="primary">Start</Button>
      <Button on:click={clearSel}  kind="ghost">Clear</Button>
      {#if loading}<Spinner />{/if}
    </div>

    <ProgressFake playing={loading} />

    <div class="text-sm text-mute">
      {files.length ? `${files.length} file(s) selected` : 'No files selected.'}
    </div>
  </div>
{:else}
  <p class="text-mute">Tool not found.</p>
{/if}
