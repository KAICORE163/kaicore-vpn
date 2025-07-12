let sessionDuration = 2 * 60 * 60; // 2 hours in seconds
let rotationInterval = 15 * 60; // 15 minutes in seconds
let sessionTimer;
let connected = false;

document.getElementById("connect-btn").onclick = async () => {
  const res = await fetch("https://kaicore-vpn.onrender.com/api/start-session");
  const data = await res.json();

  document.getElementById("ghost-id").innerText = data.ghost_id;
  document.getElementById("ip-address").innerText = data.ip;
  document.getElementById("location").innerText = data.location;

  document.getElementById("connect-btn").disabled = true;
  document.getElementById("rotate-btn").disabled = false;
  document.getElementById("disconnect-btn").disabled = false;

  connected = true;
  startTimers();
};

document.getElementById("rotate-btn").onclick = async () => {
  const res = await fetch("https://kaicore-vpn.onrender.com/api/rotate-ip");
  const data = await res.json();
  document.getElementById("ip-address").innerText = data.ip;
  document.getElementById("location").innerText = data.location;
};

document.getElementById("disconnect-btn").onclick = () => {
  connected = false;
  clearInterval(sessionTimer);
  window.location.reload();
};

function startTimers() {
  let total = sessionDuration;
  let rotate = rotationInterval;

  sessionTimer = setInterval(() => {
    if (!connected) return;

    total--;
    rotate--;

    document.getElementById("session-timer").innerText = formatTime(total);
    document.getElementById("rotation-timer").innerText = formatTime(rotate);

    if (rotate <= 0) {
      document.getElementById("rotate-btn").click();
      rotate = rotationInterval;
    }

    if (total <= 0) {
      document.getElementById("disconnect-btn").click();
    }
  }, 1000);
}

function formatTime(sec) {
  const mins = Math.floor(sec / 60);
  const secs = sec % 60;
  return `${mins}:${secs.toString().padStart(2, '0')}`;
}
