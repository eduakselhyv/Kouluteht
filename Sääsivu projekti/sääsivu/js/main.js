muutakaupunki()
async function muutakaupunki()
{
    let  e = document.getElementById("selector");
    let value = e.value;

    switch (value)
    {
        case '1':
            kaupunkimuutu('60.192059', '24.945831', 'Helsinki')
            break
        
        case '2':
            kaupunkimuutu('61.49911', '23.78712', 'Tampere')
            break
        
        case '3':
            kaupunkimuutu('63.55915', '27.19067', 'Iisalmi')
            break
        
        case '4':
            kaupunkimuutu('60.98267', '25.66151', 'Lahti')
            break
        
        case '5':
            kaupunkimuutu('61.20564', '26.03811', 'Heinola')
            break
            
    }
}

async function kaupunkimuutu(lat, lon, kaupunki) 
{
    document.getElementById('bodytag').style.backgroundImage = "url(img/"+kaupunki+".jpg)";
    let KaupunkiData = (await weatherdata(lat, lon))
    document.getElementById("u1").innerHTML = (Math.round(KaupunkiData.main.temp) - 273) + " °C";
    document.getElementById("u2").innerHTML = KaupunkiData.main.humidity + " %";
    document.getElementById("u3").innerHTML = KaupunkiData.wind.speed + " m/s";
}

async function weatherdata(lat, lon)
{
    const response = await fetch("https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=14316375e3c2d4d1f9d97b0c55d86560");
    const weather = await response.json();
    return weather;
}