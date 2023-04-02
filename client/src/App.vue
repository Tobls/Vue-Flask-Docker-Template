<template>

    <p>{{ text }}</p>

</template>
<script setup>

    import {ref} from "vue";
    import {URL_BASE} from "@/main";

    const text = ref("")

    fetch(URL_BASE + "/helloworld").then(response => response.text()).then(response => {
        text.value = response
    })

</script>