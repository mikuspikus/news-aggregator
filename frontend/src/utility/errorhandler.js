const ehandler = {
    error(vue, error, eheader, nfreason) {
        if (error.response) {
            const response = error.response
            switch (response.status) {
                case 401:
                    vue.$store.dispatch('logout', { vue: vue });
                    vue.$router.push({ name: 'Login' });
                    break;

                case 404:
                    vue.$router.push({ name: 'NotFound', params: { reason: nfreason } });
            }
        }
        else {
            vue.$bvToast.toast(error.message, {
                title: eheader,
                autoHideDelay: 5000,
                toaster: "b-toaster-bottom-center"
            });
        }
    }
}

export default ehandler