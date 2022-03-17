export default {
    data() {
        return {
            createDatasetError: '',
            datasetNameInput: '',
            datasetId: '',
            masterVmInput: '',
            selectedTask: '',
            trainingCheck: true,
            devCheck: false,
            testCheck: true,
            evaluatorWorkingDirectory: '',
            evaluatorCommand: '',
            evaluationMeasures: '',
            taskList: [],
        }
    },
    emits: ['addnotification'],
    props: ['csrf'],
    methods: {
        async get(url) {
            const response = await fetch(url)
            if (!response.ok) {
                throw new Error(`Error fetching endpoint: ${url} with ${response.status}`);
            }
            let results = await response.json()
            if (results.status === 1) {
                throw new Error(`${results.message}`);
            }
            return results
        },
        async submitPost(url, params) {
            const headers = new Headers({
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': this.csrf
            })

            const response = await fetch(url, {
                method: "POST",
                headers,
                body: JSON.stringify(params)
            })
            if (!response.ok) {
                throw new Error(`Error fetching endpoint: ${url} with ${response.status}`);
            }
            let results = await response.json()
            if (results.status === 1) {
                throw new Error(`${results.message}`);
            }
            return results
        },
        addDataset() {
            console.log('add dataset')
            this.adddatasetError = ''
            if (this.selectedTask === '') {
                this.adddatasetError += 'Please select a Task;\n'
            }
            if (this.datasetNameInput === '') {
                this.adddatasetError += 'Please provide a name for the new Dataset;\n'
            }
            if (!(this.trainingCheck || this.devCheck || this.testCheck)) {
                this.adddatasetError += 'Please declare if you create a training, test, and/or dev dataset for this name\n'
            }
            if (this.adddatasetError !== '') {
                return
            }
            this.submitPost('tira-admin/add-dataset', {
                'dataset_id': this.datasetId,
                'name': this.datasetNameInput,
                'master_id': this.masterVmInput,
                'task': this.selectedTask.task_id,
                'training': this.trainingCheck,
                'dev': this.devCheck,
                'test': this.testCheck,
                'evaluator_working_directory': this.evaluatorWorkingDirectory,
                'evaluator_command': this.evaluatorCommand,
                'evaluation_measures': this.evaluationMeasures,
            }).then(message => {
                this.$emit('addnotification', 'success', message.message)
            }).catch(error => {
                console.log(error)
                this.adddatasetError = error
            })
        },
        string_to_slug(str) {
            str = str.replace(/^\s+|\s+$/g, ''); // trim
            str = str.toLowerCase();

            // remove accents, swap ñ for n, etc
            var from = "àáäâèéëêìíïîòóöôùúüûñç·/_,:;";
            var to = "aaaaeeeeiiiioooouuuunc------";
            for (var i = 0, l = from.length; i < l; i++) {
                str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
            }

            str = str.replace(/\./g, '-')
                .replace(/[^a-z0-9 -]/g, '') // remove invalid chars
                .replace(/\s+/g, '-') // collapse whitespace and replace by -
                .replace(/-+/g, '-'); // collapse dashes

            return str;
        },
    },
    beforeMount() {
        this.get(`/api/task-list`).then(message => {
            this.taskList = message.context.task_list
        }).catch(error => {
            this.$emit('addnotification', 'error', `Error loading task list: ${error}`)
        })
    },
    watch: {
        datasetNameInput(newName, oldName) {
            this.datasetId = this.string_to_slug(newName)
        }
    },
    template: `
<div class="uk-grid-small uk-margin-small" uk-grid>
    <div class="uk-margin-right">
        <h2>Add Dataset</h2>
    </div>
</div>
<div class="uk-margin-small">
    <div class="uk-width-1-5">
        Dataset ID Prefix: [[ this.datasetId ]] 
    </div>
    <div class="uk-grid-small uk-margin-small" uk-grid>
        <div class="uk-width-1-4">
            <label for="dataset-name-input">Dataset Name*</label>
            <input id="dataset-name-input" class="uk-input" type="text" placeholder="Name of the Dataset"
                   :class="{'uk-form-danger': (this.createDatasetError !== '' && this.datasetNameInput === '')}"
                   v-model="datasetNameInput">
        </div>
        <div class="uk-width-1-4">
            <label for="task-select">Task*</label>
            <select id="task-select" class="uk-select" v-model="this.selectedTask"
                   :class="{'uk-form-danger': (this.createDatasetError !== '' && this.selectedTask === '')}">
                <option disabled value="">Please select a task</option>
                <option v-for="task in this.taskList" :value="task">[[ task.task_id ]]</option>
            </select>
        </div>
        <div class="uk-width-1-4">
            <div>
                <input id="training-check" class="uk-checkbox uk-margin-small-right" type="checkbox" v-model="trainingCheck"><label for="training-check">training</label>
            </div>
            <div>
                <input id="dev-check" class="uk-checkbox uk-margin-small-right" type="checkbox" v-model="devCheck"><label for="dev-check">dev</label>
            </div>
            <div>
                <input id="test-check" class="uk-checkbox uk-margin-small-right" type="checkbox" v-model="testCheck"><label for="test-check">test</label>
            </div>
        </div>
    </div>
    <div class="uk-margin-right">
        <h2>Evaluator</h2>
    </div>
    <div class="uk-grid-small uk-margin-small" uk-grid>
        <div class="uk-width-1-3">
            <label for="evaluator-working-directory">Evaluator Working Directory</label>
            <input id="evaluator-working-directory" type="text" class="uk-input" placeholder="/path/to/directory - Defaults to home."
                   v-model="evaluatorWorkingDirectory" />
        </div>
        <div class="uk-width-1-3">
            <label for="evaluator-command">Evaluator Command</label>
            <input id="evaluator-command" type="text" class="uk-input" placeholder="Command to be run from working directory"
                   v-model="evaluatorCommand" />
        </div>
        <div class="uk-width-1-3">
            <label for="master-vm-input">Master VM</label>
            <input id="master-vm-input" class="uk-input" type="text" placeholder="id-lowercase-with-dashes"
                   :class="{'uk-form-danger': (this.createDatasetError !== '' && this.masterVmInput === '')}"
                   v-model="masterVmInput">
        </div>
    </div>
    <div class="uk-margin-small">
        <label for="evaluation-measures">Evaluation Measures</label>
        <textarea id="evaluation-measures" rows="4" class="uk-textarea" placeholder="Measure Name,measure_key\nName will be displayed to the users.\nmeasure_key must be as output by the evaluation software."
               v-model="evaluationMeasures" />
   </div>
    <div class="uk-margin-small">
        <button class="uk-button uk-button-primary" @click="addDataset">Add Dataset</button>
        <span class="uk-text-danger uk-margin-small-left">[[ this.createDatasetError ]]</span>
    </div>
    *mandatory
</div>`
}