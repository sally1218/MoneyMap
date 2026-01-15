// 預先宣告全域變數
let zoom = 17; // 0 - 18
let center = [22.9970861, 120.2104083]; // 中心點座標-台南火車站
let map;
let marker;

// 跟使用者要位置
function successGPS(position) {
  const lat = position.coords.latitude;
  const long = position.coords.longitude;
  center = [lat, long];
  
  // 更新地圖中心
  map.setView(center, zoom);
  
  // 更新標記位置
  marker.setLatLng(center);
  marker.setPopupContent('你現在的位置');
}

function errorGPS() {
  window.alert('無法判斷您的所在位置，無法使用此功能。預設地點將為 台南火車站');
  // 使用預設位置 center
  map.setView(center, zoom);
  marker.setLatLng(center);
  marker.setPopupContent('預設位置：台南火車站');
}

if(navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(successGPS, errorGPS);
  // 持續監測位置
  navigator.geolocation.watchPosition(successGPS);
} else {
  window.alert('您的裝置不具備GPS，無法使用此功能');
}

// *** 放置地圖
map = L.map('map').setView(center, zoom);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap', // 商用時必須要有版權出處
  zoomControl: true , // 是否秀出 - + 按鈕
}).addTo(map);

// *** 放置標記
marker = L.marker(center, {
  title: '你的位置', 
  opacity: 1.0
}).bindPopup('初始位置').addTo(map);

map.locate({
  setView: false, // 是否讓地圖跟著移動中心點
  watch: true, // 是否要一直監測使用者位置
  maxZoom: 18, // 最大的縮放值
  enableHighAccuracy: true, // 是否要高精準度的抓位置
  timeout: 10000 // 觸發locationerror事件之前等待的毫秒數
});