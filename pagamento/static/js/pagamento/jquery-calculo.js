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

$(document).ready(function() {
    $("#id_categoria, #id_qtd_horas, #id_valor_hora, #id_qtd_dependente_irpf, #id_valor_pensao").on('keyup change', function() {
        var vbruto = parseInt($('#id_valor_bruto').val()) || 0;
        var qhora = parseInt($('#id_qtd_horas').val()) || 0;
        var vhora = parseInt($('#id_valor_hora').val()) || 0;
        var qdep = parseInt($('#id_qtd_dependente_irpf').val()) || 0;
        var cteg = $("#id_categoria option:selected").val();

        // calculo valor bruto
        var vbruto = qhora * vhora;
        // calculo iss 5%
        var iss_tmp = vbruto * 0.05;
        var iss = parseFloat(iss_tmp.toFixed(2));
        // calculo inss 11%
        var inss_tmp = vbruto * 0.11;
        var inss = parseFloat(inss_tmp.toFixed(2));
        // calculo para valor base para saber aliquota
        var vbase_tmp = vbruto - inss;
        var vbase = parseFloat(vbase_tmp.toFixed(2));
        // calculo patronal 20%
        var ptnal_tmp = vbruto * 0.20;
        var ptnal = parseFloat(ptnal_tmp.toFixed(2));
        // calculo deducao irpf
        var dirpf_tmp = inss+(qdep*189.59);
        var dirpf = parseFloat(dirpf_tmp.toFixed(2));
        // calculo pos deducao irpf
        var pos_irpf_tmp = vbruto-inss;
        var pos_irpf = parseFloat(pos_irpf_tmp.toFixed(2));


// Calculos para Colaborador/Professor Interno do IFMA e COLUN
        if (cteg == 1 || cteg == 3) {
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(0);
            $('#id_valor_iss').val(0);
            $('#id_deducao_irpf').val(0);
            $('#id_valor_pos_deducao_irpf').val(0);
            $('#id_valor_irpf').val(0);
            $('#id_valor_patronal').val(ptnal);
            $('#id_valor_liquido').val(vbruto);
        }
// Calculos para Colaborador/Professor Externo
        else if (vbase <= 1903.98){
            var irpf = 0;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            var vliq_tmp = vbruto-inss-iss-irpf;
            var vliq = parseFloat(vliq_tmp.toFixed(2));
            $('#id_valor_liquido').val(vliq);
        }
        else if (vbase >= 1903.99 && vbase <= 2826.65){
            var aliquota = 0.075;
            var parc_deduzir = 142.80;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            // calculo irpf
            var irpf_tmp = (vbruto-qdep-inss)*aliquota-parc_deduzir;
            var irpf = parseFloat(irpf_tmp.toFixed(2));
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            // calculo valor liquido
            var vliq_tmp = vbruto-inss-iss-irpf;
            var vliq = parseFloat(vliq_tmp.toFixed(2));
            $('#id_valor_liquido').val(vliq);
        }
        else if (vbase >= 2826.66 && vbase <= 3751.05){
            var aliquota = 0.15;
            var parc_deduzir = 354.80;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            // calculo irpf
            var irpf_tmp = (vbruto-qdep-inss)*aliquota-parc_deduzir;
            var irpf = parseFloat(irpf_tmp.toFixed(2));
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            // calculo valor liquido
            var vliq_tmp = vbruto-inss-iss-irpf;
            var vliq = parseFloat(vliq_tmp.toFixed(2));
            $('#id_valor_liquido').val(vliq);
        }
        else if (vbase >= 3751.06 && vbase <= 4664.68){
            var aliquota = 0.225;
            var parc_deduzir = 636.13;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            // calculo irpf
            var irpf_tmp = (vbruto-qdep-inss)*aliquota-parc_deduzir;
            var irpf = parseFloat(irpf_tmp.toFixed(2));
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            // calculo valor liquido
            var vliq_tmp = vbruto-inss-iss-irpf;
            var vliq = parseFloat(vliq_tmp.toFixed(2));
            $('#id_valor_liquido').val(vliq);
        }
        else if (vbase > 4664.68){
            var aliquota = 0.275;
            var parc_deduzir = 869.36;
            $('#id_valor_bruto').val(vbruto);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            // calculo irpf
            var irpf_tmp = (vbruto-qdep-inss)*aliquota-parc_deduzir;
            var irpf = parseFloat(irpf_tmp.toFixed(2));
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            // calculo valor liquido
            var vliq_tmp = vbruto-inss-iss-irpf;
            var vliq = parseFloat(vliq_tmp.toFixed(2));
            $('#id_valor_liquido').val(vliq);
            }
    });
});