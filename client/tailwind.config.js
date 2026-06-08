export default {

  content: [

    "./index.html",

    "./src/**/*.{js,ts,jsx,tsx}"
  ],

  theme: {

    extend: {

      colors: {

        primary: "#22c55e",

        secondary: "#0f172a",

        accent: "#38bdf8",

        danger: "#ef4444",

        warning: "#f59e0b"
      },

      boxShadow: {

        glass:
          "0 8px 32px 0 rgba(31, 38, 135, 0.37)"
      },

      backdropBlur: {

        xs: "2px"
      },

      backgroundImage: {

        dashboard:
          "linear-gradient(to right, #020617, #0f172a)",

        card:
          "linear-gradient(to bottom right, rgba(30,41,59,0.7), rgba(15,23,42,0.8))"
      },

      borderRadius: {

        xl2: "1.5rem"
      },

      animation: {

        float:
          "float 6s ease-in-out infinite",

        pulseSlow:
          "pulse 4s infinite"
      },

      keyframes: {

        float: {

          "0%, 100%": {
            transform:
              "translateY(0px)"
          },

          "50%": {
            transform:
              "translateY(-10px)"
          }
        }
      }
    }
  },

  plugins: []
};