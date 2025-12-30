$(document).ready(function(){
    let products = [];
    let cart = JSON.parse(localStorage.getItem("cart"))|| [];

    // load products via AJAX
    $.getJSON("product.json", function(data){
        products = data;
        renderProducts(products);
    });

    // render product carts
    function renderProducts(list){
        $("#product-list").html("");
        $.each(list, function(index, product){
            $("#product-list").append(`
                <div class="product">
                <img src="${product.img}" alt="${product.name}" onerror="this.src='images/default.jpg'">
                <h3>${product.name}</h3>
                <p>₹${product.price}</p>
                <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
                </div>
            `);
        })
    }

    // search functionality
    $("#search").on("keyup", function() {
    const searchText = $(this).val().toLowerCase();
    const filtered = products.filter(p => p.name.toLowerCase().includes(searchText));
    renderProducts(filtered);
  });

// add to cart
 $(document).on("click", ".add-to-cart", function() {
    const id = $(this).data("id");
    const product = products.find(p => p.id === id);
    const existing = cart.find(c => c.id === id);
    if (existing) {
      existing.qty += 1;
    } else {
      cart.push({ ...product, qty: 1 });
    }
    updateCart();
    Swal.fire('Added!', `${product.name} added to cart!`, 'success');
  });

//   update cart count and localstorage
function updateCart(){
    localStorage.setItem("cart", JSON.stringify(cart));
    $("#cart-count").text(cart.length);
}

// open cart
$("#cart-btn").click(function(){
    renderCart();
    $("#cart-modal").fadeIn();
});

// close cart
$("#close-cart").click(function() {
    $("#cart-modal").fadeOut();
  });

//   render cart items
function renderCart(){
     $("#cart-items").html("");
    let total = 0;

    if (cart.length === 0) {
      $("#cart-items").html("<p>Your cart is empty.</p>");
    }

    $.each(cart, function(index, item) {
      const itemTotal = item.price * item.qty;
      total += itemTotal;

      $("#cart-items").append(`
        <li class="cart-item">
          <span>${item.name}</span>
          <div>
            <span class="qty-btn decrease" data-id="${item.id}">-</span>
            ${item.qty}
            <span class="qty-btn increase" data-id="${item.id}">+</span>
            <span>₹${itemTotal}</span>
            <button class="remove-item" data-id="${item.id}">X</button>
          </div>
        </li>
      `);
    });

    $("#total").text(total);
}

// quantity increase/decrease
$(document).on("click", ".increase", function() {
    const id = $(this).data("id");
    const item = cart.find(i => i.id === id);
    item.qty += 1;
    updateCart();
    renderCart();
  });

    $(document).on("click", ".decrease", function() {
    const id = $(this).data("id");
    const item = cart.find(i => i.id === id);
    if (item.qty > 1) {
      item.qty -= 1;
    } else {
      cart = cart.filter(i => i.id !== id);
    }
    updateCart();
    renderCart();
  });

//   remove from cart
$(document).on("click", ".remove-item", function() {
    const id = $(this).data("id");
    cart = cart.filter(item => item.id !== id);
    updateCart();
    renderCart();
  });

// checkout
 $("#checkout").click(function() {
    if (cart.length === 0) {
      Swal.fire('Your cart is empty!', 'warning');
      return;
    }

    Swal.fire({
      title: 'Confirm Checkout?',
      text: 'Do you want to proceed with your order?',
      icon: 'question',
      showCancelButton: true,
      confirmButtonText: 'Yes, Checkout!',
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire('Success!', 'Your order has been placed!', 'success');
        cart = [];
        updateCart();
        renderCart();
        $("#cart-modal").fadeOut();
      }
    });
  });

//   initial cart load
updateCart();
});