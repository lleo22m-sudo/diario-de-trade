document.getElementById('registroTrade').addEventListener('submit', async function(event) {
    event.preventDefault(); // Impede o envio tradicional do formulário (que recarregaria a página)

    const form = event.target;
    const data = {
        ativo: form.ativo.value,
        entrada: form.entrada.value,
        saida: form.saida.value,
        // Campos de estudo manual:
        maxNegativo: form.maxNegativo.value,
        potencialPos: form.potencialPos.value,
        tradeConectado: form.tradeConectado.value || null // Opcional
    };

    try {
        // OBS: O Render está hospedado em HTTPS, vamos usar a rota relativa /api/...
        const response = await fetch('/api/registrar_trade', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            alert(`SUCESSO! Trade registrado em ${data.ativo}. Pips/Pontos: ${result.pips_ganhos.toFixed(2)}. Mensagem: ${result.message}`);
            form.reset(); // Limpa o formulário após o sucesso
        } else {
            alert(`ERRO: ${result.message || 'Falha na comunicação com o servidor.'}\nDetalhe: ${result.error}`);
        }
    } catch (error) {
        console.error('Erro de rede/comunicação:', error);
        alert('Erro ao conectar com o servidor. Verifique sua conexão.');
    }
});
