from IPython.core.display import display, HTML

esconde_codigo_str = '''
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Esconder código"></form>
'''

esconde_codigo_prepara_str = '''
    <script>
    function code_toggle() {
        if ($('div.cell.code_cell.rendered.selected div.input').css('display')!='none'){
            $('div.cell.code_cell.rendered.selected div.input').hide();
        } else {
            $('div.cell.code_cell.rendered.selected div.input').show();
        }
    }
    </script>

'''

display(HTML(esconde_codigo_prepara_str + esconde_codigo_str))

def esconde_codigo():
    display(HTML(esconde_codigo_str))
