const wrapper = document.querySelector(".wrapper"),
selectBtn = wrapper.querySelector(".select-btn"),
searchInp = wrapper.querySelector("input"),
options = wrapper.querySelector(".options");

const wrapper2 = document.querySelector(".wrapper2"),
selectBtn2 = wrapper2.querySelector(".select-btn"),
searchInp2 = wrapper2.querySelector("input"),
options2 = wrapper2.querySelector(".options");

const wrapper3 = document.querySelector(".wrapper3"),
selectBtn3 = wrapper3.querySelector(".select-btn"),
searchInp3 = wrapper3.querySelector("input"),
options3 = wrapper3.querySelector(".options");


function updateName(group_tag)
{
    wrapper.classList.remove("active");
    
    group_name = group_tag.innerHTML;
    sid = group_tag.getAttribute('sid')
    gr = group_tag.getAttribute('gr')

    window.open(`/api/groups?group=${group_name}&sid=${sid}&gr=${gr}`);
}


function updateName2(teacher_tag)
{
    wrapper2.classList.remove("active");
    
    teacher_name = teacher_tag.innerHTML;
    teacher_id = teacher_tag.getAttribute('value');

    window.open(`/api/teachers?teacher=${teacher_name}&teacher_id=${teacher_id}`);
}

function updateName3(cabinet_tag)
{
    wrapper3.classList.remove("active");
    
    cabinet_name = cabinet_tag.innerHTML;
    cabinet_id = cabinet_tag.getAttribute('value');

    window.open(`/api/cabinets?cabinet=${cabinet_name}&cabinet_id=${cabinet_id}`);
}


selectBtn.addEventListener("click", () => {
    wrapper.classList.toggle("active");

    wrapper2.classList.remove('active');
    wrapper3.classList.remove('active');

    options2.scrollTo(top);
    options3.scrollTo(top);
});

selectBtn2.addEventListener("click", () => {
    wrapper2.classList.toggle("active");

    wrapper.classList.remove('active');
    wrapper3.classList.remove('active');
});

selectBtn3.addEventListener("click", () => {
    wrapper3.classList.toggle("active");

    wrapper.classList.remove('active');
    wrapper2.classList.remove('active');
});


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


loadNewContent()