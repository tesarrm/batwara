<template>
    <div>
        <h2>Your Friends</h2>

        <!-- <pre>{{ JSON.stringify(friendsResource.list, null, 2) }}</pre> -->

        <div v-if="friends">
            <ol>
                <li v-for="friend in friends" key="friend">
                    <Avatar 
                        size="xl" 
                        :label="friend.full_name" 
                        :url="friend.user_image" 
                    /> 
                    {{ friend.full_name }}
                </li>
            </ol>
        </div>
    </div>
</template>

<script setup>
import {computed} from "vue";
import {createListResource, Avatar} from "frappe-ui";
import {sessionUser} from "../data/session";

const friendsResource = createListResource({
    doctype: "Friend Mapping",
    fields: [
        "b as friend",
        "b.full_name as full_name", 
        "b.user_image as user_image", 
    ],
    filters: {
        "a": sessionUser()
    },
    auto: true,
    orderBy: "b",
    // onSuccess(d) {
    //     console.log(d);
    // },
    transform(data) {
        return data.map(friend => friend.friend)
    }
})

const friends = computed(() => {
    return friendsResource.list.data || [];
})

// function getInitials(fullName) {
//     return fullName.split(" ").map(part => part[0].toUpperCase()).join("");
// }
</script>
