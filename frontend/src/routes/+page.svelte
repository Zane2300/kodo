<script lang="ts">
    import Dropzone from '$lib/components/Dropzone.svelte';

    let selectedFile: File | null = null;
    
    let isProcessing = false;
    let statusMessage = "";
    let downloadUrl: string | null = null;

    async function uploadAndConvert() {
        if (!selectedFile) return;

        isProcessing = true;
        statusMessage = "> INICIANDO UPLOAD AL SERVIDOR...";
        downloadUrl = null; 

        const formData = new FormData();
        formData.append("file", selectedFile);

        try {
            statusMessage = "> PROCESANDO EN EL NÚCLEO (FFMPEG)...";
            
            const response = await fetch("http://localhost:8000/convert", {
                method: "POST",
                body: formData
        });

        const result = await response.json();

        if (result.status === "success") {
            statusMessage = "> CONVERSIÓN COMPLETADA CON ÉXITO.";
            downloadUrl = result.download_url;
        } else {
            statusMessage = `> ERROR CRÍTICO: ${result.message}`;
            console.error(result);
        }

        } catch (error) {
            statusMessage = "> ERROR DE CONEXIÓN CON EL SERVIDOR.";
            console.error(error);
        } finally {
            isProcessing = false;
        }
    }
</script>

<div class="min-h-screen bg-[#050505] text-white font-mono flex flex-col items-center justify-center p-4">
    <div class="mb-12 text-center">
        <h1 class="text-6xl font-black tracking-tighter text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-600 drop-shadow-[0_0_10px_rgba(34,211,238,0.5)]">
            KODO
        </h1>
        <p class="mt-2 text-cyan-700 uppercase tracking-[0.3em] text-sm">
            // Swiss Army Knife v1.0
        </p>
    </div>

    <Dropzone bind:file={selectedFile} />

    {#if selectedFile}
        <div class="mt-8 p-4 border border-green-900 bg-green-900/10 rounded max-w-md w-full">
        
            <p class="text-green-500 text-xs mb-2">> SYSTEM LOG:</p>
            <code class="text-xs text-gray-400 break-all block mb-4">
                Target acquired: {selectedFile.name}<br>
                Size: {selectedFile.size} bytes<br>
                Type: {selectedFile.type || 'Unknown'}
            </code>
            
            <div class="flex flex-col gap-2">
                
                {#if !isProcessing && !downloadUrl}
                <button 
                    on:click={uploadAndConvert}
                    class="w-full bg-cyan-600 hover:bg-cyan-500 text-black font-bold py-3 px-4 rounded transition-all tracking-wider shadow-[0_0_15px_rgba(8,145,178,0.5)] hover:shadow-[0_0_25px_rgba(8,145,178,0.8)]"
                >
                    [ EJECUTAR PROTOCOLO DE CONVERSIÓN ]
                </button>
                {/if}

                {#if isProcessing}
                    <div class="w-full bg-black border border-cyan-900 p-3 text-center">
                        <p class="text-cyan-400 animate-pulse font-mono">{statusMessage}</p>
                        <div class="w-full h-1 bg-gray-800 mt-2 overflow-hidden">
                        <div class="h-full bg-cyan-500 animate-[width_2s_ease-in-out_infinite] w-1/2"></div>
                        </div>
                    </div>
                {/if}

                {#if downloadUrl}
                    <div class="w-full bg-green-900/20 border border-green-500 p-4 text-center animate-bounce-in">
                        <p class="text-green-500 font-bold mb-2">> ARCHIVO GENERADO.</p>
                        <a 
                            href={downloadUrl} 
                            target="_blank"
                            class="inline-block bg-green-600 hover:bg-green-500 text-black font-bold py-2 px-6 rounded shadow-[0_0_10px_rgba(22,163,74,0.5)]"
                        >
                            DESCARGAR RESULTADO
                        </a>
                        <button 
                            on:click={() => { selectedFile = null; downloadUrl = null; }}
                            class="block mt-2 text-xs text-gray-500 hover:text-white mx-auto underline"
                        >
                            Convertir otro archivo
                        </button>
                    </div>
                {/if}
            </div>
        </div>
    {/if}
</div>