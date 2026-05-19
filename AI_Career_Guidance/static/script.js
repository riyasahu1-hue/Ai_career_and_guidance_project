function toggleDropdown(id){

    const dropdown =
    document.getElementById(id);

    if(dropdown.style.display === "block"){
        dropdown.style.display = "none";
    }

    else{
        dropdown.style.display = "block";
    }
}

async function predictCareer(){

    const skillCheckboxes =
    document.querySelectorAll(
        '#skillsDropdown input[type="checkbox"]:checked'
    );

    const industryCheckboxes =
    document.querySelectorAll(
        '#industryDropdown input[type="checkbox"]:checked'
    );

    const skills =
    Array.from(skillCheckboxes)
    .map(cb => cb.value)
    .join(", ");

    const industry =
    Array.from(industryCheckboxes)
    .map(cb => cb.value)
    .join(", ");

    const education =
    document.getElementById("education").value;

    const experience =
    document.getElementById("experience").value;

    const response = await fetch("/predict",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            skills:skills,
            education:education,
            industry:industry,
            experience:experience
        })
    });

    const data = await response.json();

    const result =
    document.getElementById("result");

    result.style.display = "block";

    result.innerHTML = `

        <h3>${data.profession}</h3>

        <p><strong>Industry:</strong>
        ${data.industry}</p>

        <p><strong>Sector:</strong>
        ${data.sector}</p>

        <p><strong>Salary:</strong>
        ${data.salary}</p>

        <p><strong>Demand:</strong>
        ${data.demand}</p>

        <p><strong>Location:</strong>
        ${data.location}</p>

        <p><strong>Description:</strong>
        ${data.description}</p>
    `;
}