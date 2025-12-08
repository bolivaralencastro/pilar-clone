<template>
  <div class="min-h-screen">
    <!-- Background SVG -->
    <div class="fixed bottom-0 left-0 opacity-[0.02] pointer-events-none z-0 scale-[3] origin-bottom-left">
      <svg width="380" height="328" viewBox="0 0 380 328" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M95 0L0 163.917L95 327.834H285L380 163.917L285 0H95ZM252.274 307.033L34.4494 181.755L283.277 38.6387L252.274 307.033Z" fill="black"/>
      </svg>
    </div>
    <slot />
  </div>
</template>
