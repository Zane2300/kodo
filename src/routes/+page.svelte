<script lang="ts">
  import { CATEGORIES } from '$lib/data/tools';
  import Card from '$lib/components/ui/Card.svelte';
</script>

<h1 class="text-3xl mb-6 font-semibold">File Format Converters</h1>

{#each CATEGORIES as c}
  <section class="mb-10">
    <h2 class="mb-3 text-lg text-mute">{c.title}</h2>

    <!-- Grid compacto al estilo de tu dashboard -->
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-3">
      {#each c.tools as t, i}
        <!-- pasamos pequeño delay para animación escalonada -->
        <Card
          href={`/${c.slug}/${t.slug}`}
          title={t.title}
          icon={t.icon}
          delay={i * 0.04}
        />
      {/each}
    </div>
  </section>
{/each}
