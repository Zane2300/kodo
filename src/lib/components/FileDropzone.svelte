<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  let drag = false;
  function onFiles(fs: FileList | null) {
    if (!fs?.length) return;
    dispatch('select', Array.from(fs));
  }
</script>

<label
  on:dragenter|preventDefault={() => drag = true}
  on:dragleave|preventDefault={() => drag = false}
  on:dragover|preventDefault
  on:drop|preventDefault={(e)=>onFiles(e.dataTransfer?.files ?? null)}
  class="block rounded-2xl border border-dashed border-white/15 p-6 text-center cursor-pointer
         hover:border-neon/50 bg-black/30">
  <input type="file" class="hidden" on:change={(e)=>onFiles((e.target as HTMLInputElement).files)} />
  <div class="text-sm text-mute">{drag ? 'Suelta el archivo…' : 'Arrastra o haz clic para subir'}</div>
</label>
