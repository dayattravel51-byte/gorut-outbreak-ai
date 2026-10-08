// v105: legacy service worker intentionally disabled
self.addEventListener('install',event=>event.waitUntil(self.skipWaiting()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{try{const regs=await self.registration.unregister();const keys=await caches.keys();await Promise.all(keys.map(k=>caches.delete(k)));}catch(e){};return self.clients.claim();})()));
self.addEventListener('fetch',event=>{});
