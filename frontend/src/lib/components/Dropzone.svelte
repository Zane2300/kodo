<script lang="ts">
    export let file: File | null = null;
    
    let isDragging = false;
    let inputRef: HTMLInputElement;

    function handleDragEnter(e: DragEvent) {
        e.preventDefault();
        isDragging = true;
    }

    function handleDragLeave(e: DragEvent) {
        isDragging = false;
    }

    function handleDrop(e: DragEvent) {
        e.preventDefault();
        isDragging = false;

        if (e.dataTransfer?.files && e.dataTransfer.files.length > 0) {
            file = e.dataTransfer.files[0];
        }
    }

    function handleClick() {
        inputRef.click();
    }

    function handleInputChange(e: Event) {
        const target = e.target as HTMLInputElement;
        if (target.files && target.files.length > 0) {
            file = target.files[0];
        }
    }
</script>

<div
    role="button"
    tabindex="0"
    on:dragenter={handleDragEnter}
    on:dragover={handleDragEnter}
    on:dragleave={handleDragLeave}
    on:drop={handleDrop}
    on:click={handleClick}
    on:keypress={handleClick}
    class="
    relative w-full max-w-2xl p-10 
    border-2 border-dashed rounded-lg cursor-pointer
    transition-all duration-300 ease-out
    flex flex-col items-center justify-center text-center gap-4
    {isDragging 
        ? 'border-cyan-400 bg-cyan-900/20 shadow-[0_0_20px_rgba(34,211,238,0.3)] scale-[1.02]' 
        : 'border-gray-700 hover:border-cyan-700 bg-black/50'}
    "
>
    <input type="file" class="hidden" bind:this={inputRef} on:change={handleInputChange} />

    {#if file}
        <div class="text-cyan-400">
            <div class="text-4xl mb-2">📄</div>
            <p class="font-mono text-lg font-bold tracking-widest">{file.name}</p>
            <p class="text-xs text-gray-500 mt-1">{(file.size / 1024 / 1024).toFixed(2)} MB DETECTED</p>
            <p class="text-xs text-green-500 mt-2 animate-pulse">> ARCHIVO LISTO PARA PROCESAMIENTO_</p>
        </div>
    {:else}
        <div class="text-gray-400 group">
        <div class="text-5xl mb-4 opacity-50 group-hover:text-cyan-400 transition-colors">
            📥
        </div>
        <h3 class="text-xl font-bold text-gray-200 font-mono">
            INICIAR SECUENCIA DE UPLOAD
        </h3>
        <p class="text-sm mt-2 font-mono text-gray-500">
            [ ARRASTRA TU ARCHIVO AQUÍ O HAZ CLICK ]
        </p>
        </div>
    {/if}
    
    <div class="absolute top-0 left-0 w-3 h-3 border-t-2 border-l-2 border-cyan-500"></div>
    <div class="absolute top-0 right-0 w-3 h-3 border-t-2 border-r-2 border-cyan-500"></div>
    <div class="absolute bottom-0 left-0 w-3 h-3 border-b-2 border-l-2 border-cyan-500"></div>
    <div class="absolute bottom-0 right-0 w-3 h-3 border-b-2 border-r-2 border-cyan-500"></div>
</div>