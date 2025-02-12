import { defineStore } from "pinia";

export const useFootballStore = defineStore("football", {
  state: () => ({
    balls: Array.from({ length: 15 }, () => ({
      top: `${Math.random() * 100}vh`,
      left: `${Math.random() * 100}vw`,
      animationDuration: `${Math.random() * 10 + 5}s`,
      animationDelay: `${Math.random() * 2}s`
    }))
  })
});
