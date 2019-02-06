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

// Calculos para Colaborador/Professor Externo
// qh = quantidade horas; vh = valor da hora; vb = valor bruto;
$(document).ready(function() {
// Calculos para Colaborador/Professor Interno do IFMA E COLUN
// ct = categoria; st = status servidor; vl = valor liquido; vb = valor bruto
    $("#id_categoria, #id_qtd_horas, #id_valor_hora").on('keyup change', function() {
// alíquota inss



        var vb = parseInt($('#id_valor_bruto').val()) || 0;
        var qh = parseInt($('#id_qtd_horas').val()) || 0;
        var vh = parseInt($('#id_valor_hora').val()) || 0;
        var ct = $("#id_categoria option:selected").val();

        // calcula valor bruto
        var vb = qh * vh;
        // calcula iss 5%
        var iss = vb * 0.05

        if (ct == 1 || ct == 3) {
            $('#id_valor_bruto').val(vb);
            $('#id_valor_base_desc_inss').val(0);
            $('#id_valor_base_desc_iss').val(0);
            $('#id_valor_deducao_irpf').val(0);
            $('#id_valor_pos_deducao_irpf').val(0);
            $('#id_valor_irpf').val(0);
            $('#id_valor_patronal').val(0);
            $('#id_valor_liquido').val(vb);
        }
        // calculo de INSS
        else if (vb <= 1556.94){
                $('#id_valor_bruto').val(vb);
                $('#id_valor_deducao_irpf').val(null);
                // calcula inss 8%
                var inss = vb * 0.08
                $('#id_valor_base_desc_inss').val(inss);
                $('#id_valor_base_desc_iss').val(iss);
                $('#id_valor_deducao_irpf').val(null);
                $('#id_valor_pos_deducao_irpf').val(null);
                $('#id_valor_irpf').val(null);
                $('#id_valor_liquido').val(null);
                $('#id_valor_patronal').val(null);
        }
        else if (vb >= 1556.95 && vb <= 2594.92){
                $('#id_valor_bruto').val(vb);
                $('#id_valor_deducao_irpf').val(null);
                // calcula inss 9%
                var inss = vb * 0.09
                $('#id_valor_base_desc_inss').val(inss);
                $('#id_valor_base_desc_iss').val(iss);
                $('#id_valor_deducao_irpf').val(null);
                $('#id_valor_pos_deducao_irpf').val(null);
                $('#id_valor_irpf').val(null);
                $('#id_valor_liquido').val(null);
                $('#id_valor_patronal').val(null);
        }
        else if (vb >= 2594.93 && vb <= 5189.82){
                $('#id_valor_bruto').val(vb);
                $('#id_valor_deducao_irpf').val(null);
                // calcula inss 11%
                var inss = vb * 0.11
                $('#id_valor_base_desc_inss').val(inss);
                $('#id_valor_base_desc_iss').val(iss);
                $('#id_valor_deducao_irpf').val(null);
                $('#id_valor_pos_deducao_irpf').val(null);
                $('#id_valor_irpf').val(null);
                $('#id_valor_liquido').val(null);
                $('#id_valor_patronal').val(null);
        }
         else if (vb > 5189.82){
                $('#id_valor_bruto').val(vb);
                $('#id_valor_deducao_irpf').val(null);
                // inss alíquota máxima
                var inss = 570.88
                $('#id_valor_base_desc_inss').val(inss);
                $('#id_valor_base_desc_iss').val(iss);
                $('#id_valor_deducao_irpf').val(null);
                $('#id_valor_pos_deducao_irpf').val(null);
                $('#id_valor_irpf').val(null);
                $('#id_valor_liquido').val(null);
                $('#id_valor_patronal').val(null);
        }
        //calculo de IRPF
        else if (vb <= 1903.98){
                $('#id_valor_bruto').val(vb);
                $('#id_valor_deducao_irpf').val(null);
                $('#id_valor_base_desc_inss').val(inss);
                $('#id_valor_base_desc_iss').val(iss);
                $('#id_valor_deducao_irpf').val(null);
                $('#id_valor_pos_deducao_irpf').val(null);
                // calculo iRPF
                var irpf = 0;
                $('#id_valor_irpf').val(irpf);
                $('#id_valor_liquido').val(null);
                $('#id_valor_patronal').val(null);
        }

    });
});