function delete_product(id){
    Swal.fire({
        title: "¿Estás seguro de eliminar este producto?",
        text: "Este cambio no se puede revertir!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si, eliminarlo!"
    }).then(function(result){
        if(result.isConfirmed){
            window.location.href="/eliminar/"+id+"/"
        }
    });
}
function modify_product(id) {
    Swal.fire({
        title: "¿Estás seguro de modificar este producto?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Sí, modificarlo!"
    }).then(function(result) {
        if (result.isConfirmed) {
            document.getElementById('edit-product-form').submit();
        }
    });
}