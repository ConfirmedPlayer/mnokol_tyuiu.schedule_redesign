function NoWhitespace(event)
{
  if (event.which == 32)
    {
      event.preventDefault();
      return false;
    }
}


var loadNewContent = function() {
  $.ajax('/data/groups', {
    success: function(response)
    {
      $('#parent_options').html(response);
      pkst_20_9_2 = document.getElementById('ПКСт-20-(9)-2').outerHTML
      document.getElementById('ПКСт-20-(9)-2').remove()
      document.getElementById('parent_options').insertAdjacentHTML('afterbegin', pkst_20_9_2);
      document.getElementById('ПКСт-20-(9)-2').style.textShadow = '0px 0px 0px #000000';
    }
  });
  $.ajax('/data/teachers', {
    success: function(response)
    {
      $('#parent_options2').html(response);
    }
  });
  $.ajax('/data/cabinets', {
    success: function(response)
    {
      $('#parent_options3').html(response);
    }
  });
};


function filterFunction()
{
  var input, filter, a, i;
  input = document.getElementById("mainInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("parent_options");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    }else {
      a[i].style.display = "none";
    }
  }
}


function filterFunction2()
{
  var input, filter, a, i;
  input = document.getElementById("mainInput2");
  filter = input.value.toUpperCase();
  div = document.getElementById("parent_options2");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    }else {
      a[i].style.display = "none";
    }
  }
}


function filterFunction3()
{
  var input, filter, a, i;
  input = document.getElementById("mainInput3");
  filter = input.value.toUpperCase();
  div = document.getElementById("parent_options3");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    }else {
      a[i].style.display = "none";
    }
  }
}