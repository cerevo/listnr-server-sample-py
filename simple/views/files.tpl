<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Uploaded files</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
</head>
<body>

<div class="container">
    <h1>Listnr audio</h1>
</div>

<div class="container">
    <div class="col-md-12">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Time</th>
                    <th>Player</th>
                    <th>File</th>
                </tr>
            </thead>
            <tbody>
                % for file in files:
                <tr>
                    <th scope="row" class="time" data-time="{{file['time']}}"></th>
                    <td><audio src="{{file['url']}}" controls></audio></td>
                    <td><a href="{{file['url']}}" download><img src="../img/ic_file_download_black_24dp_2x.png" width="24" height="24"></a></td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>

<script src="js/main.js"></script>
</body>
</html>
