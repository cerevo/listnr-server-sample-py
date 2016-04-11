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
    <h1>Listnr speech to text</h1>
</div>

<div class="container">
    <div class="col-md-12">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Time</th>
                    <th>Text</th>
                    <th>File</th>
                </tr>
            </thead>
            <tbody>
                % for log in logs:
                <tr>
                    <th scope="row" class="time" data-time="{{log['created_at']}}"></th>
                    <td class="log">{{log['text']}}</td>
                    <td><a href="/files/{{log['filename']}}"><img src="../img/ic_file_download_black_24dp_2x.png" width="24" height="24"></a></td>
                </tr>
                % end
            </tbody>
        </table>
    </div>
</div>

<script src="js/main.js"></script>
</body>
</html>
