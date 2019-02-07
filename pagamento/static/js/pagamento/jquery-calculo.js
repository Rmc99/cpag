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

        // calcula valor bruto
        var vb = qh * vh;
        // calcula iss 5%
        var iss = vb * 0.05;
        // calcula inss 11%
        var inss = vb * 0.11;
        // calcula patronal 20%
        var ptnal = vb * 0.20;

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
            var dirpf = inss+(qdep*189.59);
            var pos_irpf = vb-inss;
            var vl = vb-inss-iss;

            $('#id_valor_bruto').val(vb);
            $('#id_valor_inss').val(inss);
            $('#id_valor_iss').val(iss);
            $('#id_deducao_irpf').val(dirpf);
            $('#id_valor_pos_deducao_irpf').val(pos_irpf);
            $('#id_valor_irpf').val(irpf);
            $('#id_valor_patronal').val(ptnal);
            $('#id_valor_liquido').val(vl);
        }
  /*          else {
            }
        }
        else if (vb >= 1556.95 && vb <= 2594.92){
        }
        else if (vb >= 2594.93 && vb <= 5189.82){
        }
         else if (vb > 5189.82){
        }
  */
    });
});