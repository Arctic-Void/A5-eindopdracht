<!doctype html>
<html lang="nl">

<head>
    <meta charset="utf-8">
    <title>Fair play in de VOORBEELD-DIVISIE</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="stylesheet" href="css/normalize.css">
    <link rel="stylesheet" href="css/main.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon" />
    <link rel="preconnect" href="https://fonts.gstatic.com">

    <!-- Hier worden de fonts al voor je ingeladen! -->
    <link
        href="https://fonts.googleapis.com/css2?family=Faster+One&family=Roboto:ital,wght@0,400;0,500;0,700;1,400;1,500&family=Roboto+Mono:wght@400;500&display=swap"
        rel="stylesheet">
</head>

<body>

    <div class="container">
        <div class="wrapper">
            <header>
                <h1>Voorbeeld Divisie</h1>
                <p class="subtitle">Fair-play website</p>
            </header>

            <main>
                <p>De SPORT-bond ziet toe op een eerlijk verloop van de competitie. Onze topsporters dienen een
                    voorbeeld te zijn voor de vele amateurs in de sport. Daarom streven we naar <em>fair play</em>; een
                    sportieve omgang met elkaar. Daar hoort ook bij dat er weinig overtredingen plaatsvinden tijdens een
                    wedstrijd. Op deze website geven we inzicht in het verloop van de competitie tot nu toe. U ziet de
                    wedstrijden met de minste overtredingen, maar voor bewustwording brengen we ook de wedstrijden met
                    de <em>meeste</em> overtredingen in beeld.</p>
                <div class="row">
                    <div class="box half">
                        <h2>Aantal overtredingen:</h2>
                        <p class="number">
                            <?php echo 3115 ?>
                        </p>
                    </div>
                    <div class="box half2">

                        <h2>Gemiddeld per wedstrijd:</h2>
                        <p class="number">
                            <?php echo 8 ?>
                        </p>

                    </div>
                </div>

                <div class="column">
                    <div class="box">
                        <div class="box1">

                            <h2>Wedstrijden met de meeste overtredingen:</h2>
                            <pre><?php
                            echo file_get_contents('backend/zwartboek.txt');
                            ?></pre>
                        </div>
                        <div class="box2">
                            <h2>Wedstrijden met 1 of minder overtredingen in de laatste 21 dagen:</h2>
                            <pre><?php
                            echo file_get_contents('backend/eregalerij.txt');
                            ?></pre>
                        </div>
                    </div>
                </div>
            </main>

            <footer>
                <p>Deze website is gemaakt in het kader van een praktijkopdracht bij de opleiding Software Developer,
                    Curio Breda.</p>
                <p>&copy; Berend, Dani en Zouhir.</p>
            </footer>
        </div>
    </div>

</body>

</html>