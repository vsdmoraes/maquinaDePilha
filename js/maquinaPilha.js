window.onload = function() {
        var fileInput = document.getElementById('fileInput');

        fileInput.addEventListener('change', function(e) {
            var file = fileInput.files[0];
            var textType = /text.*/;

            if (file.type.match(textType)) {
                var reader = new FileReader();
                //console.log(reader.result);

                reader.onload = function(e) {
                    document.getElementById('fileOut').innerText = reader.result;
                }

                reader.readAsText(file); 
                
            } else {
                document.getElementById('fileOut').innerText = "Erro: Formato não suportado!"
            }

            document.getElementById('read').style.display="none";
        });
}