const ehandler = {
    feedparseerror(error) {
        if (error.response) {
            const response = error.response;
            return { data: response.data.error, code: response.status }
        }

        return { data: error.message, code: null }
    },
    formerror(error) {
        if (error.response) {
            const response = error.response;
            return { data: response.data, code: response.status }
        }

        return { data: error.message, code: null }
    },
    loginerror(error) {
        if (error.response) {
            const response = error.response;
            return { msg: response.data.detail, code: response.status }
        }

        return { msg: error.message, code: null }
    },
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