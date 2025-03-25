self.addEventListener("install", event => {
    console.log("Service Worker Installed");
    event.waitUntil(
        caches.open("medium-reader").then(cache => {
            return cache.addAll([
                "/",
                "/static/index.html",
                "/static/style.css"
            ]);
        })
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});
