const list_str = `
/media/photos/20220201_121513.jpg
/media/photos/IMG_20201220_141802__01.jpg
/media/photos/subtest/test.mp4
`

// execute `{ echo "const list_str = \`"; find /media/photos/ -type f; echo "\`"; cat slideshow/without_list.js; } > slideshow/with_list.js` in order to generate the working script

let album = "/"

function showAlbum(name)
{
	album = name
	console.log("only picking files from album", name)
	document.getElementById("albums").style.display = "none"
}

function load()
{
	const socket = io("https://raps.hilkojj.nl")
	socket.on("temperature", temp => document.getElementById("temp").innerHTML = Math.round(temp * 10)/10)
	socket.on("humidity", humid => document.getElementById("humid").innerHTML = Math.round(humid * 10)/10)
	socket.emit("request_sensor_data")

    
    const files = list_str.split("\n").filter(entry => entry.length > 0)
    const baseSlashIndex = Math.min(...files.map(entry => entry.lastIndexOf('/')))

    console.log(files.length + " files found!")

    const albums = ["/", ...new Set(
        files.filter(entry => entry.lastIndexOf('/') > baseSlashIndex)
            .map(entry => entry.substring(baseSlashIndex))
            .map(entry => entry.substring(0, entry.lastIndexOf("/")))
    )]
	const albumsListElement = document.getElementById("albums")

    console.log(albums.length + " albums found!")
	albums.forEach(entry => {
		albumsListElement.innerHTML += `
			<li onclick="showAlbum('`+entry+`')">`+entry+`</li>
		`
	})

    const photoElement = document.getElementById("photo")
    const videoElement = document.getElementById("video")

	photoElement.onclick = videoElement.onclick = () => albumsListElement.style.display = "flex"

    function showRandom() {

	const candidates = files.filter(entry => entry.substring(baseSlashIndex).startsWith(album))

        const fileSrc = candidates[Math.floor(Math.random() * candidates.length)]
	console.log("time to show", fileSrc)

	const isVideo = fileSrc.endsWith(".mp4")

	if (isVideo) apply()
	else
	{
		const preloadImg = new Image()
		preloadImg.src = fileSrc
		preloadImg.onload = apply
		preloadImg.onerror = showRandom
	}

	function apply()
	{

		const mediaElement = isVideo ? videoElement : photoElement;

		(mediaElement == photoElement ? videoElement : photoElement).style.display = "none"
		mediaElement.style.display = "block"
		mediaElement.src = fileSrc

		if (isVideo)
		{
			videoElement.onended = showRandom
			document.getElementById("blurred").style.backgroundImage = "none"
		}
		else
		{
			setTimeout(showRandom, 3000)
			document.getElementById("blurred").style.backgroundImage = `url("` + fileSrc + `")`
		}
	}

    }

	showRandom()
}
window.onload = load

