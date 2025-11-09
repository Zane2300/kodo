<script lang="ts">
  import favicon from '$lib/assets/favicon.svg';
  import '../app.css';
  import Sidebar from '$lib/components/Sidebar.svelte';
  import Topbar from '$lib/components/Topbar.svelte';
  import CommandPalette from '$lib/components/CommandPalette.svelte';
</script>

<svelte:head>
  <link rel="icon" href={favicon} />
</svelte:head>

<div aria-hidden="true"
     class="pointer-events-none fixed inset-0 -z-10
            bg-[radial-gradient(1000px_500px_at_20%_-10%,rgba(244,63,94,.10),transparent),
                radial-gradient(1000px_500px_at_110%_-10%,rgba(34,211,238,.10),transparent)]">
</div>

<div class="min-h-screen bg-bg text-ink font-[Inter,_system-ui,sans-serif]">
  <Topbar />
  <div class="mx-auto max-w-[1400px] px-4 md:px-6 lg:px-8">
    <div class="grid grid-cols-12 gap-6 py-6">
      <aside class="col-span-12 md:col-span-3 lg:col-span-2">
        <Sidebar />
      </aside>
      <main class="col-span-12 md:col-span-9 lg:col-span-10 bg-black/5 rounded-2xl">
        <slot />
      </main>
    </div>
  </div>
</div>

<CommandPalette />
