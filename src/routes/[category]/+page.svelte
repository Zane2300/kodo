<script lang="ts">
  import { CATEGORIES } from '$lib/data/tools';
  import Card from '$lib/components/ui/Card.svelte';
  import { page } from '$app/stores';

  // 👇 estas dos líneas son reactivas
  $: slug = $page.params.category;
  $: cat = CATEGORIES.find((c) => c.slug === slug);
</script>

{#if cat}
  <h1 class="text-2xl mb-6">{cat.title}</h1>
  <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
    {#each cat.tools as t}
      <Card href={`/${cat.slug}/${t.slug}`} title={t.title} icon={t.icon} />
    {/each}
  </div>
{:else}
  <p class="text-mute">Category not found.</p>
{/if}