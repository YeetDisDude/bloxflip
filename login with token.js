let token = "your token";

function login(token) {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage._DO_NOT_SHARE_BLOXFLIP_TOKEN = `${token}`
    location.reload();
  }

login(token);
