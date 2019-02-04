$(document).ready(
    function () {
        var $id_ano = $("#id_ano");
        $id_ano.mask('0000', {reverse: true});

        var $id_qtd_horas = $("#id_qtd_horas");
        $id_qtd_horas.mask('0000', {reverse: true});

        var $id_valor_hora = $("#id_valor_hora");
        $id_valor_hora.mask('00000', {reverse: true});

        var $id_qtd_dependente_irpf = $("#id_qtd_dependente_irpf");
        $id_qtd_dependente_irpf.mask('00', {reverse: true});
   }
);