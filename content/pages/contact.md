Title: /contact
Slug: contact


<form method="POST" action="https://formspree.io/rieger.brian12@gmail.com">
  <div class="form-group">
    <label for="reply-email">reply email</label>
    <input id="reply-email" class="form-control" name="reply-email" placeholder="your email" type="email" required>
  </div>
  <div class="form-group">
    <label for="message">message</label>
    <textarea id="message" class="form-control" name="message" placeholder="your message..." rows="7" required></textarea>
  </div>
  <button id="encrypt-message-btn" type="button" class="btn btn-primary">
    <i class="fa fa-lock" aria-hidden="true"></i>
    encrypt message
  </button>
  <button type="submit" class="btn btn-success">
    <i class="fa fa-send" aria-hidden="true"></i>
    send
  </button>
</form>

<script type="text/javascript" src="{filename}/js/openpgp.min.js"></script>
<script type="text/javascript" src="{filename}/js/jquery.min.js"></script>
<script>
  var pubkey = openpgp.key.readArmored(
    "-----BEGIN PGP PUBLIC KEY BLOCK-----\n" +
    "Version: GnuPG v1\n" +
    "\n" +
    "mQENBFjO+/gBCADMM9YHB5eMwzpR4tvSk/zQ4zVNnbL7cAviP5LnfLXCGOzQlUmp\n" +
    "sqqPhz9ypBSi6DkaMQWpgxsxQ1Z/GBYQn3rpKiEDKXeT2rYRKUohLj5LhreMCnZ4\n" +
    "80Ku0mL9p0qL0m8PHl7g+/oTzbRPsdj8DQfk4zy+UMmHuL4+9QjjApeZQ8h8uFVk\n" +
    "ShM19WdCwyns/tDwL4LHHw/TNUWOsQJVoK6OR6yGnFjV0KQAFWu9kT0rYFZdYLfL\n" +
    "Os/mJr9NcWEY2dV/MPwsD4kmPl4GeHq+JVYDchJvlakVxOeQZv68j0JvJXLuVqdo\n" +
    "fKpBLWDZdIPQ6zZHV/3lTxQBEO9BILYP/tYXABEBAAG0NEJyaWFuIENoYXJsZXMg\n" +
    "UmllZ2VyIDxicmlhbi5jLnJpZWdlckBwcm90b25tYWlsLmNvbT6JAT4EEwECACgF\n" +
    "AljO+/gCGwMFCQHhM4AGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEBaIW8LG\n" +
    "nlpZyXQIALvfunvsJ3VfYVYVLndlrokuAP0QLJHL4XyWWzsPx9H8TBp3hmK3BM/P\n" +
    "F7C+OfKxP3WNAlKFFxcvv36FfaSfASeXQR4L/C48MGkdvCQcqbdy0aqorMjSeMMm\n" +
    "AYCyT7700NX7WphWHsYRiSnnPk8Yl4SdsUSSD9JV897eSmbj8ft9s64wr02N1Hyj\n" +
    "tppygMkmlS+nZe/mEhHR38FMje6dq4c3DET13RuZyzC1IyV64KBQruqqc1do31tT\n" +
    "TWMCousG6xoMQdfg9U/IGhy1qmwdPI8SDQeJJSKsdRoceVGCgw/WCrP8l/8AbN+8\n" +
    "VERNSplDf/BcFTKfIRyohq1TN6p17zW5AQ0EWM77+AEIAMwlYx7doDaWu6F1AMfS\n" +
    "QTI2A+YHm4/K2CHZipD7SifuiJn0ePAEc8PEs3eQP2kniRctdVY02xezjLOw6zRA\n" +
    "BVvZe5LVMKMP0cIUVQzJNC7LKfRlohn/kRV6RqPEja620+yxmQGIbbEEToFQdXqH\n" +
    "xgFFKS285nBI3pBjVFyYPqtArN5C/2kSV7+nQsJ3RDcSoC3TSvTqZKiXpdGwOuf7\n" +
    "BLXlhgFj25Lb81S5vLvOSZM2m4Es1TLgdkQLmy/6oClGSHpNsUQzyU4+5dU64BTY\n" +
    "LIEYbFih9vcrNW32BKu9nXfbvbdRP3zCVQxyxr4imeWz7EDzb8ZZa+dm3BLoPdpf\n" +
    "W+EAEQEAAYkBJQQYAQIADwUCWM77+AIbDAUJAeEzgAAKCRAWiFvCxp5aWdTIB/wN\n" +
    "xR9AIuwybgS/flx2TcIZ7K/JufB9RqJw2crb8ntXMPya2egSr0QlOGmRWcYk7DGz\n" +
    "JQj1mOQWAt4/PBXyHQvGFdTJ0WURx4SeRhkNI3wnFP1s9/tmntG42aTc7pHKaWGq\n" +
    "3x8/Ibe508ms25URSlZ5o6Va0U2gSPkokO7fGk/W/4wZy9MtrEV4sibpcchGy5c8\n" +
    "NaRZyN01xkw4v8OLrNKCwOl5Dcs1kKkFJIpuOAsrNZQpo7hvj9zJOq5AmV/OJKME\n" +
    "lRYTITGh4xgu4XFLw8uQAGddo4eCrv6NI/8ewl/5P0mCGhsjF4e69c+6DLIvO2O1\n" +
    "nBsQuVlHP7CM8HS5NJ4C\n" +
    "=fgmg\n" +
    "-----END PGP PUBLIC KEY BLOCK-----"
  );

  $(document).ready(function() {
    $('#encrypt-message-btn').click(function() {
      options = {
        data: $('#message').val(),
        publicKeys: pubkey.keys,
        armor:true
      };
      openpgp.encrypt(options).then(function(ciphertext) {
        $('#message').val(ciphertext.data);
      }, function(failObj) {
        console.log(failObj);
        alert('failed to encrypt message');
      });
    });
  });
</script>
