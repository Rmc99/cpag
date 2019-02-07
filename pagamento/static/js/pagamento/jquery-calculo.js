// Deixa somente leitura e na cor cinza os campos
    $('#id_valor_bruto').prop('readonly', true);
    $("#id_valor_bruto").css('background', '#DCDCDC');
    $('#id_valor_inss').prop('readonly', true);
    $("#id_valor_inss").css('background', '#DCDCDC');
    $('#id_valor_iss').prop('readonly', true);
    $("#id_valor_iss").css('background', '#DCDCDC');
    $('#id_deducao_irpf').prop('readonly', true);
    $("#id_deducao_irpf").css('background', '#DCDCDC');
    $('#id_valor_pos_deducao_irpf').prop('readonly', true);
    $("#id_valor_pos_deducao_irpf").css('background', '#DCDCDC');
    $('#id_valor_irpf').prop('readonly', true);
    $("#id_valor_irpf").css('background', '#DCDCDC');
    $('#id_valor_liquido').prop('readonly', true);
    $("#id_valor_liquido").css('background', '#DCDCDC');
    $('#id_valor_patronal').prop('readonly', true);
    $("#id_valor_patronal").css('background', '#DCDCDC');

// Descrição das variaveis utilizadas:
// 'qh' = quantidade horas; 'vh' = valor da hora; 'vb' = valor bruto;
// 'ct' = categoria; 'vl' = valor liquido; 'vb' = valor bruto; 'ptnal' = patronal;

$(document).ready(function() {
    $("#id_categoria, #id_qtd_horas, #id_valor_hora, #id_qtd_dependente_irpf, #id_valor_pensao").on('keyup change', function() {
        var vb = parseInt($('#id_valor_bruto').val()) || 0;
        var qh = parseInt($('#id_qtd_horas').val()) || 0;
        var vh = parseInt($('#id_valor_hora').val()) || 0;
        var qdep = parseInt($('#id_qtd_dependente_irpf').val()) || 0;
        var ct = $("#id_categoria option:selected").val();

        // calculo valor bruto
        var vb = qh * vh;
        // calculo iss 5%
        var iss_tmp = vb * 0.05;
        var iss = parseFloat(iss_tmp.toFixed(2));
        // calculo inss 11%
        var inss_tmp = vb * 0.11;
        var inss = parseFloat(inss_tmp.toFixed(2));
        // calculo patronal 20%
        var ptnal_tmp = vb * 0.20;
        var ptnal = parseFloat(ptnal_tmp.toFixed(2));
        // calculo deducao irpf
        var dirpf_tmp = inss+(qdep*189.59);
        var dirpf = parseFloat(dirpf_tmp.toFixed(2));
        // calculo pos deducao irpf
        var pos_irpf = vb-inss;
        // calculo valor liquido
        var vl = vb-inss-iss;

// Calculos para Colaborador/Professor Interno do IFMA e COLUN
        if (ct == 1 || ct == 3) {
            $('#id_valor_bruto').val(vb);
            $('#id_valor_inss').val(0);
            $('#id_valor_iss').val(0);
            $('#id_deducao_irpf').val(0);
            $('#id_valor_pos_deducao_irpf').val(0);
            $('#id_valor_irpf').val(0);
            $('#id_valor_patronal').val(ptnal);
            $('#id_valor_liquido').val(vb);
        }
// Calculos para Colaborador/Professor Externo
        else if (vb <= 1903.98){
            var irpf = 0;
            $('#id_valor_bruto').val(vb);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            $('#id_valor_liquido').val(vl);
        }
        else if (vb >= 1903.99 && vb <= 2826.65){
            aliquota = 0.075;
            $('#id_valor_bruto').val(vb);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            $('#id_valor_liquido').val(vl);
        }
    });
});