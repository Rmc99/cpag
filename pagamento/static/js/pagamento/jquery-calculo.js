$(document).ready(function() {
    $("#id_valor_hora").on('keyup', function() {
        var qh = parseInt($('#id_qtd_horas').val()) || 0;
        var vh = parseInt($('#id_valor_hora').val()) || 0;
        // calcula valor bruto
        var vb = qh * vh;
        // calcula inss 11%
        var inss = vb * 0.11
        // calcula iss 5%
        var iss = vb * 0.05

        // exibe valor bruto
        $('#id_valor_bruto').val(vb);
        // exibe inss
        $('#id_valor_base_desc_inss').val(inss);
        // exibe iss
        $('#id_valor_base_desc_iss').val(iss);
        // Aqui teremos que fazer os calculos de acordo com o QTD de dependentes


    });
});

// Deixa somente leitura e na cor cinza os campos
$('#id_valor_bruto').prop('readonly', true);
$("#id_valor_bruto").css('background', '#DCDCDC');
$('#id_valor_base_desc_inss').prop('readonly', true);
$("#id_valor_base_desc_inss").css('background', '#DCDCDC');
$('#id_valor_base_desc_iss').prop('readonly', true);
$("#id_valor_base_desc_iss").css('background', '#DCDCDC');
$('#id_valor_deducao_irpf').prop('readonly', true);
$("#id_valor_deducao_irpf").css('background', '#DCDCDC');
$('#id_valor_pos_deducao_irpf').prop('readonly', true);
$("#id_valor_pos_deducao_irpf").css('background', '#DCDCDC');
$('#id_valor_irpf').prop('readonly', true);
$("#id_valor_irpf").css('background', '#DCDCDC');
$('#id_valor_liquido').prop('readonly', true);
$("#id_valor_liquido").css('background', '#DCDCDC');
$('#id_valor_patronal').prop('readonly', true);
$("#id_valor_patronal").css('background', '#DCDCDC');